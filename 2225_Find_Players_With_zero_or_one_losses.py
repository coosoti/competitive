class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = [0] * 1000000 
        for winner, loser in matches:
            if losses[winner] == 0:
                losses[winner] = -1

            if losses[loser] == -1:
                losses[loser] = 1
            else:
                losses[loser] += 1

        no_loss = [i for i in range(1000000) if losses[i] == -1]
        one_loss = [i for i in range(1000000) if losses[i] == 1]

        return [no_loss, one_loss]