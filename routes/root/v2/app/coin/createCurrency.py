from flask import request, render_template_string
from src.common.template import centeredHtml

def main():
    return {
            "status": "QUEUED",
            "contract_address": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
            "transaction_id": "4872e8c0-3e7a-43df-ac15-ba894919cf33",
            "transaction_hash": "0x51103659d8827d6d24732d1168de73390f4f387d58a8281944241657f1bc61d7",
            "transaction_chain_scan_url": "https://polygonscan.com/tx/0x51103659d8827d6d24732d1168de73390f4f387d58a8281944241657f1bc61d7"
        }