import imaplib
import util
configinfo = util.load_config()

# IMAP 서버 정보
IMAP_SERVER = configinfo["mail"]["IMAP_SERVER"]
IMAP_PORT = 993  # IMAP SSL 기본 포트
USERNAME = configinfo["login"]["EMAIL"]
PASSWORD = configinfo["login"]["PW"]

def test_imap_connection():
    """IMAP 연결 테스트"""
    try:
        # IMAP 서버에 SSL로 연결
        print(f"IMAP 서버에 연결 시도 중: {IMAP_SERVER}:{IMAP_PORT}")
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        
        # 로그인 시도
        print(f"{USERNAME} 계정으로 로그인 시도 중...")
        mail.login(USERNAME, PASSWORD)
        
        # 연결 성공
        print("IMAP 연결 및 로그인 성공!")
        
        # 받은 편지함 선택
        mail.select("inbox")
        print("받은 편지함 선택 성공!")

        # 로그아웃
        mail.logout()
        print("IMAP 연결 테스트 종료.")
    
    except imaplib.IMAP4.error as e:
        print(f"IMAP 연결 실패: {e}")
    
    except Exception as e:
        print(f"오류 발생: {e}")

# 실행
if __name__ == "__main__":
    test_imap_connection()
