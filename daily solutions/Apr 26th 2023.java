class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};

class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }

public class Apr26th2023 {

    // #117 Populating Next Right Pointers in Each Node II (BFS)
    public Node connect(Node root) {
        if (root == null) return null; // return if tree is null

        Node cur = root; // initialize current parent level iterator

        while (true) {
            Node head = null; // initialize head list node to null
            Node p = null; // iterator p

            while (cur != null) {

                if (cur.left != null) {
                    if (head == null) { // if this is the first non-null child
                        head = cur.left; // update head
                        p = head; // initialize iterator p
                    }
                    else { // if not first non-null child
                        p.next = cur.left; // establish connection for prev non-null child
                        p = p.next; // make this node up next for connection
                    }
                }

                if (cur.right != null) {
                    if (head == null) { // if this is the first non-null child
                        head = cur.right; // update head
                        p = head; // initialize iterator p
                    }
                    else { // if not first non-null child
                        p.next = cur.right; // establish connection for prev non-null child
                        p = p.next; // make this node up next for connection
                    }
                }
                cur = cur.next; // move to next inline element in parent
            }

            if (head == null) break; // all children are null => no next level

            cur = head; // make current child level the parent level
        }

        return root; // done
    }

    // #572 Subtree of Another Tree
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) // if we reached an end
            return false;

        if (isSame(root, subRoot)) // if these trees are identical
            return true;

        // use dfs to check children
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean isSame(TreeNode one, TreeNode two) { // Check if trees are identical
        if (one == null && two == null)
            return true;

        if (one == null || two == null || one.val != two.val)
            return false;

        return isSame(one.left, two.left) && isSame(one.right, two.right);
    }

}
