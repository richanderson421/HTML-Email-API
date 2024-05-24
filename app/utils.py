from jinja2 import Environment, FileSystemLoader

def generate_email_html(subject, recipient_name, message_body, product_details):
    env = Environment(loader=FileSystemLoader('app/templates'))
    template = env.get_template('email_template.html')
    email_html = template.render(
        subject=subject,
        recipient_name=recipient_name,
        message_body=message_body,
        product_details=product_details
    )
    return email_html
