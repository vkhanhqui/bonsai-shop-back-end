import json
import requests


SENDGRID_API_URL = 'https://api.sendgrid.com/v3/mail/send'
SENDGRID_API_KEY = \
    ''


def send_msg_via_sendgrid(
    template_id: str, email_to: str,
    dynamic_template_data: dict
) -> None:
    payload = json.dumps({
        'personalizations': [
            {
                'to': [
                    {
                        'email': email_to
                    }
                ],
                'dynamic_template_data': dynamic_template_data
            }
        ],
        'from': {
            'email': 'quivo.greenlife@vkhanhqui.xyz',
            'name': 'GreenLife'
        },
        'template_id': template_id
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + SENDGRID_API_KEY
    }
    _ = requests.post(
        url=SENDGRID_API_URL, headers=headers,
        data=bytes(payload, encoding='utf-8'),
    )
