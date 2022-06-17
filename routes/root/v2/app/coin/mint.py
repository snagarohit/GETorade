from flask import request, render_template_string
from src.common.template import centeredHtml

def main():
    return {
  "status": "QUEUED",
  "transactionUrl": "https://polygonscan.com/tx/0xb2620b28c018a6746a34860b6fe5344510ee533abcf0e6552e6ed07fc4e93494",
  "transactionHash": "0xb2620b28c018a6746a34860b6fe5344510ee533abcf0e6552e6ed07fc4e93494",
  "transactionId": "c41f4c5f-1480-4ab2-8122-e65d939e05f1"
}