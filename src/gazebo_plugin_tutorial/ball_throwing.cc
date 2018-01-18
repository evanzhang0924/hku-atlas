#include <boost/bind.hpp>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <stdio.h>


namespace gazebo
{
  class BallModelPlugin : public ModelPlugin
  {
    public: BallModelPlugin() : ModelPlugin()
    {
        printf("BallModelPlugin !\n");
    }



    public: void OnUpdate(const common::UpdateInfo & _info)
    {
        this->info = _info;

        double simTimeDouble = this->info.simTime.Double();
        int simTimeInt = int(simTimeDouble);

        if(simTimeInt % 6 == 0 && !isThrown) {

            this->model->SetGravityMode(true);
            this->isThrown = true;
            this->model->SetLinearVel(math::Vector3(-3, 0.19, 6.6));
        }

        if((simTimeInt + 3) % 6 == 0) {
            this->model->SetGravityMode(false);
            this->isThrown = false;
            this->model->SetLinkWorldPose(this->pose, this->lp);
            this->model->SetLinearVel(math::Vector3(0, 0, 0));
        }
        // Apply a small linear velocity to the model.
        // this->model->SetLinearVel(math::Vector3(0.03, 0, 0));

    }



    public: void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
        this->model = _model;
        this->isThrown = false;

        // Listen to the update event. This event is broadcast every
        // simulation iteration.

        this->updateConnection = event::Events::ConnectWorldUpdateBegin(
            boost::bind(&BallModelPlugin::OnUpdate, this, _1));
        this->lp = this->model->GetLink ("link");
        this->pose = this->model->GetWorldPose();

    }

    // Pointer to the model
    private: physics::ModelPtr model;

    private: common::UpdateInfo info;

    // Pointer to the update event connection
    private: event::ConnectionPtr updateConnection;

    private: bool isThrown;
    private: math::Pose pose;
    private: physics::LinkPtr lp;

  };
  GZ_REGISTER_MODEL_PLUGIN(BallModelPlugin)
}
