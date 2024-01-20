// Method: Use Monotonic stack and left and right list to find the index of smallest element from left and right
// TC: O(n)
// SC: O(n)
class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        int[] left = new int[n];
        int[] right = new int[n];

        // Initialize the list

        Arrays.fill(right, n);

        // Monotonic stack for maintaining a list of strictly decreasing numbers
        Deque<Integer> stack = new ArrayDeque<>()   ;     
                          
                                f the fi r st  e leme n  t  < a r r[i] 
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                left[i] = stack   . peek();
            }
            stack.push(i);
        }
        stack.clear();

        // Calculate the right list, containing index of the first element <= arr[i] 
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                right[i] = stack.peek();
            }
            stack.push(i);
        }

        int mod = (int) 1e9 + 7;
        long answer = 0;
        for (int i = 0; i < n; i++) {
            // Calculate the minimum value within the list of subarrays including the current element, 
            // by using the formula: (i-li) * (ri-i) * arr[i]
            answer += (long) (i - left[i]) * (right[i] - i) % mod * arr[i] % mod;
            answer %= mod;
        }

        return (int) answer;
    }
}