/*
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order, and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * Example 1
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 *
 * Example 2:
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 *
 * Example 3:
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 *
 * Constraints:
 * The number of nodes in each linked list is in the range [1, 100].
 * 0 <= Node.val <= 9
 * It is guaranteed that the list represents a number that does not have leading zeros.
  */
#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* next;
        ListNode* head;
        ListNode* curr;
        curr = new ListNode();
        head = curr;
        int sum, carry = 0;
        while (l1 != nullptr || l2 != nullptr || carry) {
            int val1 = 0, val2 = 0;
            if (l1 != nullptr){
                val1 = l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr){
                val2 = l2->val;
                l2 = l2->next;
            }
            sum = (val1 + val2 + carry) % 10;
            carry = (val1 + val2 + carry) / 10;
            curr->val = sum;
            if (l1 != nullptr || l2 != nullptr || carry) {
                next = new ListNode();
                curr->next = next;
                curr = next;
            }
        }
        return head;
    }
};

int main() {
    Solution solution;
    ListNode* l1;
    ListNode* l2;
    vector<int> a = {9,9,9,9,9,9,9};
    vector<int> b = {9,9,9,9};

    l1 = new ListNode();
    ListNode* l1_head = l1;
    for (int i = 0; i < a.size(); i++) {
        l1->val = a[i];
        if (i < a.size() - 1) {
            auto* next = new ListNode();
            l1->next = next;
            l1 = next;
        }
    }

    l2 = new ListNode();
    ListNode* l2_head = l2;
    for (int i = 0; i < b.size(); i++) {
        l2->val = b[i];
        if (i < b.size() - 1) {
            auto* next = new ListNode();
            l2->next = next;
            l2 = next;
        }
    }
    auto l3 = solution.addTwoNumbers(l1_head , l2_head);
    while (l3 != nullptr) {
        cout << l3->val << " ";
        l3 = l3->next;
    }
}

