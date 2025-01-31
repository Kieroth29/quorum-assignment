from typing import List

from schemas.votes import VoteResult, VoteTypeEnum


class LegislationService:
    @staticmethod
    def filter_vote_results(vote_results: List[VoteResult], vote_type: VoteTypeEnum) -> List[VoteResult]:
        """Return list of vote results filtered by the provided vote type."""
        return [result for result in vote_results if result.vote_type == vote_type]
