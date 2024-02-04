// Method: Use Sliding window with hashmap and go on finding the window with minimum elements count containing t's elements
// TC: O(s + t)
// SC: O(s + t)
class Solution {
    public String minWindow(String s, String t) {   
        int m = s.length(), n = t.length();
        if (m < n) {
            return "";
        }

        // Hashmap to store t's elements count
        Map<Character, Integer> map = new HashMap<>();
        for (char c : t.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        int required = map.size(), formed = 0;
        int l = 0, r = 0;
        int maxCount = 0, resLeft = 0, resRight = 0;

        // Hashmap to store window's elements count
        Map<Character, Integer> window = new HashMap<>();

        // Iterate till r reaches end
        while (r < m) {
            char c = s.charAt(r);
            window.put(c, window.getOrDefault(c, 0) + 1);

            if (map.containsKey(c) && window.get(c).intValue() == map.get(c).intValue()) {
                formed++;
            }

            // Iterate till l is less than r AND required count is not found
            while (l <= r && formed == required) {
                c = s.charAt(l);
                if (maxCount == 0 || r - l + 1 < maxCount) {
                    maxCount = r - l + 1;
                    resLeft = l;
                    resRight = r;
                }

                // Remove the elements while moving left pointer
                window.put(c, window.get(c) - 1);
                if (map.containsKey(c) && window.get(c).intValue() < map.get(c).intValue()) {
                    formed--;
                }
                l++;
            }
            r++;
        }
        
        return maxCount == 0 ? "" : s.substring(resLeft, resRight + 1);
    }
}