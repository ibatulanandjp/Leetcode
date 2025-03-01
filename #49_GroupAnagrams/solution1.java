// Method: Use Hashmap to store sortedWord: [words, ...]
// TC: O(n * m * logm)
// SC: O(n * m)
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, Integer> map = new HashMap<>();
        List<List<String>> result = new ArrayList<>();

        for (String word : strs) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);

            if (map.containsKey(sortedWord)) {
                result.get(map.get(sortedWord)).add(word);
            } else {
                map.put(sortedWord, result.size());
                result.add(new ArrayList<>(Arrays.asList(word)));
            }
        }
        return result;
    }
}