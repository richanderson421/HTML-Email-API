from flask import Blueprint, request, jsonify
from .utils import generate_email_html

email_bp = Blueprint('email_bp', __name__)

@email_bp.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    try:
        subject = data.get('subject')
        recipient_name = data.get('recipient_name')
        message_body = data.get('message_body')
        product_details = data.get('product_details', {})

        email_html = generate_email_html(subject, recipient_name, message_body, product_details)
        return jsonify({'email_html': email_html}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
