#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include <geometry_msgs/Twist.h>

float max_dist2robot = 0.3; // in meter
float min_north , min_west, min_south, min_east;
int state_flag = 0; 
// 0: Go Forward
// 1: Turn left
// 2: Turn Right
// 3: Go Backward
// 4: Stop
// 5: Go Forward Fast
// 6: Fear
// 7: Aggression
// 8: Love

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

geometry_msgs::Twist go_forward()
{
    geometry_msgs::Twist msg;
    msg.linear.x = 0.1;
    msg.angular.z = 0;
    return msg;
}

geometry_msgs::Twist go_forward_fast()
{
    geometry_msgs::Twist msg;
    msg.linear.x = 0.4;
    msg.angular.z = 0;
    return msg;
}

geometry_msgs::Twist go_backward()
{
    geometry_msgs::Twist msg;
    msg.linear.x = -0.1;
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
        state_flag = 3;
        std::cout << "North --> Go Backward" << std::endl;
    }
}

void vehicle1_positive() 
{
    if (min_north < max_dist2robot + 0.7 )
    {
        state_flag = 5;
        std::cout << "North --> Go Forward Fast" << std::endl;
    }
}  

geometry_msgs::Twist fear_msg;      
void vehicle2_fear(float west, float east) 
{
    if (east < max_dist2robot + 0.8 )
    {
      fear_msg.linear.x = 0.5;
      fear_msg.angular.z = 0.2;
      std::cout << "Fear-East" << std::endl;
      state_flag = 6;        
    } else if (west < max_dist2robot + 0.8 )
    {
      fear_msg.linear.x = 0.5;
      fear_msg.angular.z = -0.2;
      std::cout << "Fear-West" << std::endl;
      state_flag = 6;
    } else
    {
      fear_msg.linear.x = 0.2;
      fear_msg.angular.z = 0;
      std::cout << "Fear-Normal Forward" << std::endl;
      state_flag = 6;
    }

}

geometry_msgs::Twist aggr_msg;      
void vehicle2_aggression(float west, float east) 
{
    if (east < max_dist2robot + 0.8 )
    {
      aggr_msg.linear.x = 0.4;
      aggr_msg.angular.z = -0.7;
      std::cout << "Aggr-East" << std::endl;
      state_flag = 7;        
    } else if (west < max_dist2robot + 0.8 )
    {
      aggr_msg.linear.x = 0.4;
      aggr_msg.angular.z = 0.7;
      std::cout << "Aggr-West" << std::endl;
      state_flag = 7;
    } else
    {
      aggr_msg.linear.x = 0.2;
      aggr_msg.angular.z = 0;
      std::cout << "Agrr-Normal Forward" << std::endl;
      state_flag = 7;
    }
}

geometry_msgs::Twist love_msg;      
void vehicle2_love(float west, float east) 
{
    if (east < max_dist2robot + 0.8 )
    {
      if (east < max_dist2robot + 0.3)
      {
        love_msg.linear.x = 0;
        love_msg.angular.z = 0;
        state_flag = 8;        
      } else 
      {
        love_msg.linear.x = 0.1;
        love_msg.angular.z = -0.5;
        std::cout << "Love-East" << std::endl;
        state_flag = 8;
      }        
    } else if (west < max_dist2robot + 0.8 )
    {  
      if (west < max_dist2robot + 0.3)
      {
        love_msg.linear.x = 0;
        love_msg.angular.z = 0;
        state_flag = 8;        
      } else 
      {
        love_msg.linear.x = 0.1;
        love_msg.angular.z = 0.5;
        std::cout << "Love-West" << std::endl;
        state_flag = 8;
      }
    } else
    {
      love_msg.linear.x = 0.2;
      love_msg.angular.z = 0;
      std::cout << "Love-Normal Forward" << std::endl;
      state_flag = 8;
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

    //vehicle1_negative();
    //vehicle1_positive();
    //vehicle2_fear(min_west,min_east);        
    //vehicle2_aggression(min_west,min_east);
    vehicle2_love(min_west,min_east);
}



int main(int argc, char **argv)
{
  ros::init(argc, argv, "scan_listener");
  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe<sensor_msgs::LaserScan>("/scan", 1000, scanCallback);
  
  ros::Publisher pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
  ros::Rate rate(2); //2 Hz

  while(ros::ok())
  {
      geometry_msgs::Twist msg;
      msg.linear.x = 0;
      msg.angular.z = 0;
      
      if (state_flag == 0)
      {
        msg = go_forward();    
      } else if (state_flag == 1)
      {
        msg = turn_left();
      } else if (state_flag == 2)
      {
        msg = turn_right();
      } else if (state_flag == 3)
      {
        msg = go_backward();
      } else if (state_flag == 4)
      {
        msg = stop();
      } else if (state_flag == 5)
      {
        msg = go_forward_fast();
      } else if (state_flag == 6)
      {
        msg = fear_msg;
      } else if (state_flag == 7)
      {
        msg = aggr_msg;
      } else if (state_flag == 8)
      {
        msg = love_msg;
      }
      
      pub.publish(msg); //Send velocity command to robot
      rate.sleep();
      ros::spinOnce();
  }  
}
  


