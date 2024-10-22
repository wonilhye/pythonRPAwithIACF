from pyhwpx import Hwp

hwp = Hwp(new=True)  # 메인 인스턴스 생성

page_info = hwp.get_pagedef_as_dict()
page_info["왼쪽"] = 30
page_info["오른쪽"] = 30

#set 명령어 추가하기
