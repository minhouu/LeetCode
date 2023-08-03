/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode resultHead= new ListNode(0, result);
        
        while (l1 != null || l2 != null) {
            // check if l1 and l2 is null and append it's value to sum 
            int sum = 0;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;       
            }

            // check if result.val + sum is over 10. if its value is over 10, add 1 to result.next
            if (result.val + sum < 10) {
                result.val += sum;
                // when there is no more lists to add, break
                if (l1 == null && l2 == null) {
                    break;
                }
                //else, make new ListNode
                result.next = new ListNode(0);
            }
            // when result.val + sum is over 10, make new listnode which has its value of 1 
            else {
                result.val = result.val + sum - 10;
                result.next = new ListNode(1);
            }
            result = result.next;
        }
        

        return resultHead.next;
    }
}