# Global-Capstone-Design : Autonomous Driving Using Image Processing
2025 글로벌 캡스톤 디자인 - Sunmoon Univ., Silesian University of Technology

## Project Scenario
Camera와 LiDAR를 사용한 자율주행 알고리즘 제작.
1. Camera, LiDAR를 사용한 자율주행 - 라인주행, 신호등 감지, 장애물 감지 시 정지
2. LiDAR만 사용하여 앞차 따라가기
3. LiDAR만 사용하여 장애물 사이 피해가기
4. PID를 사용한 조향과 그렇지 않은 조향 차이 비교

## 👥 Team Roles
| 이름 | 역할 | 주요 담당 |
|------|------|-----------|
| 이기준 | 팀장 | Development System Setup, Programming, System Design, Scenario Development, Communication |
| 안상현 | 팀원 | 3D Design, Wire Management, H/W Assemble |
| 이원재 | 팀원 | 3D Assemble, H/W Assemble, Testing |
| 김영진 | 팀원 | Circuit Design, Wire Management, Consultation |

## ⚙️ Tech Stack
- Raspberry Pi4
- Ubuntu(20.04)+ROS, Raspbian12, OpenCV
- Python
- LiDAR, USB Camera, CSI Camera

## 📸 Project Gallery
| ![기존 차량](https://github.com/KIJUN24/Global-Capstone-Design/blob/master/Pictures%20of%20Project/%EA%B8%B0%EC%A1%B4%20%EC%B0%A8%EB%9F%89%20%EC%84%A4%EA%B3%84.png) |  ![라이다 사용을 위한 설계 수정](https://github.com/KIJUN24/Global-Capstone-Design/blob/master/Pictures%20of%20Project/%EB%9D%BC%EC%9D%B4%EB%8B%A4%20%EC%B0%A8%EB%9F%89%20%EC%84%A4%EA%B3%84.png) |
|:---:|:---:|
| 기존 차량 | 라이다 사용을 위해 설계 수정 |

| ![기존 차량](https://github.com/KIJUN24/Global-Capstone-Design/blob/master/Pictures%20of%20Project/%EA%B8%B0%EC%A1%B4%20%EC%B0%A8%EB%9F%89%20%EC%84%A4%EA%B3%84.png) | ![PID 앞 차량](https://github.com/KIJUN24/Global-Capstone-Design/blob/master/Pictures%20of%20Project/PID%20%EC%95%9E%20%EC%B0%A8%EB%9F%89%20%EC%84%A4%EA%B3%84.png) |
|:---:|:---:|
| 기존 차량 | 뒤에서 라이다를 인식시키기 위해 설계 수정 |


| ![라인 인식](https://github.com/KIJUN24/Global-Capstone-Design/blob/master/Pictures%20of%20Project/%EC%83%89%20%EA%B0%90%EC%A7%80.png) |
|:---:|
| 라인 인식 |

| ![색 감지](https://github.com/KIJUN24/Global-Capstone-Design/blob/master/Pictures%20of%20Project/%EB%9D%BC%EC%9D%B8%20%EC%9D%B8%EC%8B%9D%20%EC%82%AC%EC%A7%84.png) |
|:---:|
| 색 감지 |

| ![PID 결과](https://github.com/KIJUN24/Global-Capstone-Design/blob/master/Pictures%20of%20Project/PID%20%EC%A1%B0%ED%96%A5%20%EA%B2%B0%EA%B3%BC%EA%B0%92.png) |
|:---:|
| PID 결과 |

| ![LiDAR 감지](https://github.com/KIJUN24/Global-Capstone-Design/blob/master/Pictures%20of%20Project/%EB%9D%BC%EC%9D%B4%EB%8B%A4%20%EC%9D%B8%EC%8B%9D.png) |
|:---:|
| LiDAR 감지 |

## 🏆 Expected Outcomes
- 서보모터를 사용하여 애커만 스티어링이 가능한 자율주행 기술 구현(차선 인식 및 장애물 감지)
- 카메라를 사용하여 색 감지 -> 신호등 색 처리
- LiDAR를 사용하여 장애물 감지
- LiDAR만 사용한 자율주행1 -> 앞차 따라가기
- LiDAR만 사용한 자율주행2 -> 양쪽에 있는 장애물 회피
- 타 대학, 폴란드 학생들과 함께 프로젝트를 하며 팀 협업 능력 강화(리더십 향상)
