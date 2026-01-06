/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if(head == NULL || head->next == NULL){
        return head;
    }
    struct ListNode *curr = head;
    struct ListNode *prev = NULL;
    struct ListNode *next = NULL;

    while(curr != NULL){
        next = curr->next; //save next
        curr->next = prev; //connect back
        prev = curr; //advance prev to curr
        curr = next; //advance curr
    }
    return prev;
}