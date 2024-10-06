import random
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def draw_lottery(basic_name_list, additional_name_list):
    seat_count = 30
    assigned_count = 28

    # 기본 이름 리스트와 추가 이름 리스트를 결합
    total_name_list = basic_name_list + additional_name_list

    # 자리 배정
    assigned_names = random.sample(total_name_list, assigned_count)

    # 중복 이름 처리
    unique_names = {}

    for name in assigned_names:
        if name not in unique_names:
            unique_names[name] = 0  # 중복 카운트 초기화
        unique_names[name] += 1  # 중복 카운트 증가
        unique_name_display = f"{name}_{unique_names[name]}"  # 고유 이름 생성
        assigned_names[assigned_names.index(name)] = unique_name_display  # 배정된 이름 업데이트

    # 결과 출력
    print_table(assigned_names)


def print_table(assigned_names):
    # 한글 폰트 설정
    font_path = 'C:/Windows/Fonts/malgun.ttf'  # 예: 윈도우 경로
    # font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # 예: 리눅스 경로
    font_prop = fm.FontProperties(fname=font_path, size=12)

    # 테이블 데이터 준비
    data = [assigned_names[i:i + 10] for i in range(0, len(assigned_names), 10)]  # 10개씩 나누기

    # 테이블 생성
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')

    # 테이블 생성
    table = ax.table(cellText=data, colLabels=[f"Seat {i + 1}" for i in range(len(data[0]))], cellLoc='center',
                     loc='center')

    # 테이블 스타일 지정
    table.auto_set_font_size(False)
    table.set_fontsize(12)  # 전체 폰트 크기 설정

    for key, cell in table.get_celld().items():
        cell.set_fontsize(12)  # 각 셀의 폰트 크기 설정
        cell.set_text_props(fontproperties=font_prop)  # 각 셀의 텍스트 속성 설정

    table.scale(1.2, 1.2)  # 크기 조정

    # 테이블 출력
    plt.show()


# 미리 정의된 기본 이름 리스트
basic_name_list = [
    "Name1", "Name2", "Name3", "Name4", "Name5",
    "Name6", "Name7", "Name8", "Name9", "Name10",
    "Name11", "Name12", "Name13", "Name14", "Name15",
    "Name16", "Name17", "Name18", "Name19", "Name20",
    "Name21", "Name22", "Name23", "Name24", "Name25",
    "Name26", "Name27", "Name28"
]

# 추가 이름 입력 받기
additional_name_list = []
for _ in range(10):  # 최대 10개의 추가 이름을 입력받도록 설정
    name = input("Enter an additional name (press Enter to finish): ")
    if name == "":
        break
    additional_name_list.append(name)

# 자리 추첨 실행
draw_lottery(basic_name_list, additional_name_list)
