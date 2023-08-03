class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        // 2개, 2개로 나눠서
        // 2개의 합들을 hashmap에 저장
        // -(나머지 2개의 합)이 hashmap에 있으면
        // 있는 숫자만큼 count에 더해준다. 
        int n = nums1.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                map.put(nums1[i] + nums2[j], map.getOrDefault(nums1[i] + nums2[j], 0) + 1);
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                count += map.getOrDefault(-(nums3[i] + nums4[j]), 0);
            }
        }
        return count;
    }
}