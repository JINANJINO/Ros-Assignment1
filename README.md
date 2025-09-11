# Ros-Assignment1
로봇운영체제 실습 첫 번째 과제로써 Ros에서 기본적으로 제공되는 Package인 'turtlesim'을 이용한다.
이때 기존에는 ```turtle_teleop_key``` node를 활용하여 ```turtlesim_node```와 통신하였으나,
과제는 직접 ```Publisher``` 노드를 작성하여 ```turtlesim_node```에 있는 거북이를 움직이는 것이다.
<img width="500" height="530" alt="image" src="https://github.com/user-attachments/assets/0778f87d-fa08-4828-afa9-de8b96f13d23" />
위의 이미지에 있는 거북이에게 ```Topic```을 발행하여 ```turtlesim_node```가 구독하기 위해서는 우선 ```turtlesim```의 message type을 알 필요가 있다.
우선 먼저 키보드를 통해 조작하기 위해 Terminal 창에 ```ros2 run turtlesim turtlesim_node```와 ```ros2 run turtlesim turtle_teleop_key```
2개의 node를 실행시키자.


이후 ```ros2 topic list```를 통해서 확인하면
```
jinhan@jinhan:~$ ros2 topic list
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```
다음과 같은 topic이 존재함을 알 수 있다.
여기서, ```/turtle1/cmd_vel``` topic이 ```ros2 run turtlesim turtlesim_node```와 ```ros2 run turtlesim turtle_teleop_key``` 사이에서 거북이가 움직이도록 하는 Topic임을 알 수 있다.
이 메세지 정보를 알기 위해서 다시 터미널 창에 다음과 같은 명령어를 통해 확인한다.
```ros2 topic info /turtle1/cmd_vel```
그러면 결과 화면으로서

```
jinhan@jinhan:~$ ros2 topic info /turtle1/cmd_vel
Type: geometry_msgs/msg/Twist
Publisher count: 1
Subscription count: 1
```
가 뜨고 우리는 이 메세지가 geometry_msgs의 Twist타입인 것을 알 수 있다.
msg의 종류는 Ros 공식 사이트에 올라와 있는 document를 참고하길 바란다.
<https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Twist.html>
이를 통해서 Package를 생성할 때 의존성 파일로서 ```geometry_msgs```를 추가해야 함을 알 수 있으며, Publisher code를 작성할 때 ```from geometry_msgs.msg import Twist, Vector3```를 import해야 함을 알 수 있다.
code는 해당 repository의 파일을 참고하길 바란다.

해당 Publisher code를 실행시키면 다음과 같이 거북이가 오른쪽으로 쭉 이동함을 알 수 있다.
<img width="502" height="538" alt="Screenshot from 2025-09-11 23-29-55" src="https://github.com/user-attachments/assets/a722eefd-a687-4929-9319-0f2c4c6c4fbb" />

