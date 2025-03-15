from email.mime.text import MIMEText
from smtplib import SMTP, SMTPException

from app.config import env


def send_invite_email(
    name: str,
    email: str,
    password: str,
) -> str:
    try:
        with SMTP(host="smtp.gmail.com", port=587) as server:
            server.ehlo()
            server.starttls()
            server.login(user=env.SMTP_EMAIL, password=env.SMTP_PASSWORD)

            with open(
                "app/templates/invite_template.html",
                "r",
                encoding="utf-8",
            ) as file:
                html_content = file.read()

            html_content = html_content.replace("{recipient_name}", name)
            html_content = html_content.replace("{signup_link}", env.WEB_URL)
            html_content = html_content.replace(
                "{password}",
                f"<code>{password}</code>",
            )

            msg = MIMEText(html_content, "html")
            msg["Subject"] = "simple-RAG에 초대합니다."
            msg["From"] = env.SMTP_EMAIL
            msg["To"] = email

            server.sendmail(
                from_addr=env.SMTP_EMAIL,
                to_addrs=[email],
                msg=msg.as_string(),
            )

        return f"회원가입 초대장이 {email}로 성공적으로 발송되었습니다!"

    except SMTPException as e:
        return f"이메일 전송 실패: {e}"
    except Exception as e:
        return f"알 수 없는 오류 발생: {e}"
