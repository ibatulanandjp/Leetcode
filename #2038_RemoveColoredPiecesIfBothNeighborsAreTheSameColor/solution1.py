# Method: Use 2 pointers to count same colors, and subtract '2' for start and end characters, which should be removed in the game.
# TC: O(n), since we traverse the string once.
# SC: O(1)
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_count, bob_count = 0, 0
        l = 0
        for r in range(len(colors)):
            # If colors at left & right are different or end of string
            if colors[l] != colors[r] or r == len(colors) - 1:
                # Count the length between l and r
                length = r - l + 1 if colors[l] == colors[r] else r - l
                if length >= 3:
                    # Add to the respective count, by subtracting '2' (removing the first and last colors)
                    if colors[l] == "A":
                        alice_count += length - 2
                    else:
                        bob_count += length - 2
                l = r

        return alice_count > bob_count
