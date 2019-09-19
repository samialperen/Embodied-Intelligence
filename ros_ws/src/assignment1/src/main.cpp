#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include <geometry_msgs/Twist.h>

float max_dist2robot = 0.3; // in meter
float min_north , min_west, min_south, min_east;
int state_flag = 0; 
// 0: Go straight
// 1: Turn left
// 2: Turn Right
// 3: Stop

geometry_msgs::Twist turn_left()
{
    geometry_msgs::Twist msg;
    msg.linear.x = 0;
    msg.angular.z = 0.25;
    return msg;
}

geometry_msgs::Twist turn_right()
{
    geometry_msgs::Twist msg;
    msg.linear.x = 0;
    msg.angular.z = -0.25;
    return msg;
}

geometry_msgs::Twist go_straight()
{
    geometry_msgs::Twist msg;
    msg.linear.x = 0.1;
    msg.angular.z = 0;
    return msg;
}

geometry_msgs::Twist stop()
{
    geometry_msgs::Twist msg;
    msg.linear.x = 0;
    msg.angular.z = 0;
    return msg;
}

void vehicle1_negative() 
{
    if (min_north < max_dist2robot )
    {
        state_flag = 1;
        //turn_left();
        std::cout << "North --> Turn Left" << std::endl;
    }
} 


    
void scanCallback (const sensor_msgs::LaserScan::ConstPtr& scan_in)
{
    int count = scan_in->scan_time / scan_in->time_increment;
    //ROS_INFO("I heard a laser scan %s[%d]:", scan_in->header.frame_id.c_str(), count);
    
    
    min_north = scan_in->ranges[0];
    // North Side of The Robot
    for (int i=0; i<10;i++)
    {
        if(min_north>scan_in->ranges[i])
        {
            min_north = scan_in->ranges[i];
        }
    }
    
    
    min_west = scan_in->ranges[90];
    // West Side of The Robot
    for (int i=90; i<100; i++)
    {
        if(min_west>scan_in->ranges[i])
        {
            min_west = scan_in->ranges[i];
        }
    }
    
    min_south = scan_in->ranges[180];
    // South Side of The Robot
    for (int i=180; i<190; i++)
    {
        if(min_south>scan_in->ranges[i])
        {
            min_south = scan_in->ranges[i];
        }
    }
    
    min_east = scan_in->ranges[270];
    // South Side of The Robot
    for (int i=270; i<280; i++)
    {
        if(min_east>scan_in->ranges[i])
        {
            min_east = scan_in->ranges[i];
        }
    }
    
    //std::cout << "Size: " << scan_in->ranges.size() << std::endl;
    std::cout << "North: " << min_north << std::endl;
    std::cout << "West: " << min_west << std::endl;
    std::cout << "South: " << min_south << std::endl;
    std::cout << "East: " << min_east << std::endl;

    vehicle1_negative();        
}



int main(int argc, char **argv)
{
  ros::init(argc, argv, "scan_listener");
  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe<sensor_msgs::LaserScan>("/scan", 1000, scanCallback);
  
  ros::Publisher pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
  ros::Rate rate(2);

  while(ros::ok())
  {
      geometry_msgs::Twist msg;
      msg.linear.x = 0;
      msg.angular.z = 0;
      
      if (state_flag == 0)
      {
        msg = go_straight();    
      } else if (state_flag == 1)
      {
        msg = turn_left();
      } else if (state_flag == 2)
      {
        msg = turn_right();
      } else if (state_flag == 3)
      {
        msg = stop();
      }
      
      pub.publish(msg); //Send velocity command to robot
      rate.sleep();
      ros::spinOnce();
  }  
}
  


