class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # helper
        # good  -> a set of letters that push the current diagonal forward
        # score -> running total for this diagonal (+1 for good, -1 for others)
        # bad   -> how many “-1” moves we have seen so far
        # best  -> best distance we could reach up to this point
        def best_for(good):
            score = 0
            bad   = 0
            best  = 0

            for ch in s:
                if ch in good:         # a helpful step
                    score += 1
                else:                  # an unhelpful step
                    score -= 1
                    bad   += 1

                # we may flip at most k of those bad moves
                # every flip changes -1 into +1, so adds +2
                best = max(best, score + 2 * min(k, bad))

            return best

        # try each diagonal and return the largest distance
        return max(
            best_for({'N', 'E'}),   # x + y
            best_for({'N', 'W'}),   # -x + y
            best_for({'S', 'E'}),   # x - y
            best_for({'S', 'W'})    # -x - y
        )