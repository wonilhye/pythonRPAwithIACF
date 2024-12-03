import imaplib
import email
import util
import os
from email.header import decode_header
from datetime import datetime, timedelta

configinfo = util.load_config()

# 로그인 정보
IMAP_SERVER = configinfo["mail"]["IMAP_SERVER"]
EMAIL_ACCOUNT = configinfo["login"]["EMAIL"]
EMAIL_PASSWORD = configinfo["login"]["PW"]
SEARCHKEYWORD = configinfo["setting"]["SEARCHKEYWORD"]
DOWNLOAD_FOLDER = "C:\\Users\\onewo\\Downloads\\ihfolder"

# IMAP 연결 및 로그인
def connect_to_imap():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        return mail
    except Exception as e:
        print(f"IMAP 연결 실패: {e}")
        return None

# 첨부파일 저장
def save_attachment(part, download_folder, filename):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    filepath = os.path.join(download_folder, filename)
    with open(filepath, "wb") as f:
        f.write(part.get_payload(decode=True))
    print(f"첨부파일 저장 완료: {filepath}")

# 받은 편지함에서 최근 2일 이메일 읽기 및 첨부파일 다운로드
def read_and_download_attachments():
    mail = connect_to_imap()
    if mail is None:
        return

    try:
        mail.select("inbox")
        two_days_ago = (datetime.now() - timedelta(days=2)).strftime('%d-%b-%Y')
        status, messages = mail.search(None, f'SINCE {two_days_ago}')
        if status != "OK":
            print("이메일 검색 실패")
            return
        
        email_ids = messages[0].split()
        print(f"최근 2일 동안 {len(email_ids)}개의 이메일이 있습니다.")
        
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            if status != "OK":
                print(f"이메일 ID {email_id} 가져오기 실패")
                continue
            
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    
                    if SEARCHKEYWORD in subject:
                        print(f"제목: {subject}")
                        
                        # 첨부파일 처리
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_disposition() == "attachment":
                                    filename, encoding = decode_header(part.get_filename())[0]
                                    if isinstance(filename, bytes):
                                        filename = filename.decode(encoding if encoding else "utf-8")
                                    save_attachment(part, DOWNLOAD_FOLDER, filename)
    finally:
        mail.logout()

if __name__ == "__main__":
    read_and_download_attachments()
