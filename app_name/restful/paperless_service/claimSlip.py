# app_name/paperless_service/claimSlip.py

from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
from .structure import *

class ClaimSlip(Structure):
    permission_classes = [permissions.AllowAny]
    def __init__(self):
        super().__init__("claim_slip_systems", "claim_slip_index", "slip")


