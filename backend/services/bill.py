from typing import List

from schemas.bill import Bill, BillFileData
from schemas.legislator import LegislatorFileData
from schemas.votes import VoteResult, VoteTypeEnum
from services.legislation import LegislationService
from utils.data import import_data


class BillService(LegislationService):
    def list_bills(self) -> List[Bill]:
        """List all bills' IDs, names, their primary sponsors (if applicable) and number of supporters or opposers."""
        data = import_data()

        legislators_data: List[LegislatorFileData] = data['legislators']
        bills_data: List[BillFileData] = data['bills']
        bills: List[Bill] = []

        for bill in bills_data:
            primary_sponsor = next((
                legislator.name.split(' (')[0] for legislator in legislators_data if legislator.id == bill.sponsor_id), None)

            bill_vote_results: List[VoteResult] = [
                result for result in data['vote_results'] if result.vote_id == bill.id]

            supporters = len(
                [result for result in bill_vote_results if result.vote_type == VoteTypeEnum.SUPPORT])
            opposers = len(
                [result for result in bill_vote_results if result.vote_type == VoteTypeEnum.OPPOSE])

            bills.append(Bill(id=bill.id, bill=bill.title, primary_sponsor=primary_sponsor,
                         supporters=supporters, opposers=opposers))

        return bills
