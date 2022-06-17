from flask import request, render_template_string
from src.common.template import centeredHtml

def main():
  json_req = request.json
  txnId = json_req['transactionId']
  
  if txnId == "4872e8c0-3e7a-43df-ac15-ba894919cf33":
    txnHash = "0x51103659d8827d6d24732d1168de73390f4f387d58a8281944241657f1bc61d7"
  else:
    txnHash = "0xb2620b28c018a6746a34860b6fe5344510ee533abcf0e6552e6ed07fc4e93494"
  
  return {
  "status": "COMPLETED",
  "transactionUrl": "https://mumbai.polygonscan.com/tx/" + txnHash,
  "transactionHash": txnHash
}