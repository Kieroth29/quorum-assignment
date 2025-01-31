from typing import List

from schemas.votes import VoteResult, VoteTypeEnum
from schemas.legislator import Legislator, LegislatorFileData
from services.legislation import LegislationService
from utils.data import import_data


class LegislatorService(LegislationService):
    def list_legislators(self) -> List[Legislator]:
        """List all legislators' IDs, names and number of supported or opposed bills."""
        data = import_data()

        legislators_data: List[LegislatorFileData] = data['legislators']
        legislators: List[Legislator] = []

        for legislator in legislators_data:
            legislator_vote_results: List[VoteResult] = [
                result for result in data['vote_results'] if result.legislator_id == legislator.id]

            supported_bills = len(self.filter_vote_results(
                legislator_vote_results, VoteTypeEnum.SUPPORT))
            opposed_bills = len(self.filter_vote_results(
                legislator_vote_results, VoteTypeEnum.OPPOSE))

            legislator.name = legislator.name.split(' (')[0]

            legislators.append(Legislator(
                id=legislator.id, legislator=legislator.name, supported_bills=supported_bills, opposed_bills=opposed_bills))

        return legislators
