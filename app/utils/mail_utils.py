import json
import requests


SENDGRID_API_URL = 'https://api.sendgrid.com/v3/mail/send'
SENDGRID_API_KEY = \
    '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'


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


template_id = 'd-ed854d393e1c4eb08f15d685f1d34fa3'
email_to = 'vkhanhqui@gmail.com'
dynamic_template_data = {
    "total_price": 1099.0020
}
_ = send_msg_via_sendgrid(
    template_id,
    email_to,
    dynamic_template_data
)
