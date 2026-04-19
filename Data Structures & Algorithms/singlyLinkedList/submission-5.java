class Node {
    private int value;
    private Node next;

    public Node(int value) {
        this(value, null);
    }

    public Node(int value, Node next) {
        this.value = value;
        this.next = next;
    }

    public int getValue() {
        return value;
    }

    public void setNext(Node n) {
        this.next = n;
    }

    public Node getNext() {
        return this.next;
    }
}

class LinkedList {
    private Node head;
    private Node tail;

    public LinkedList() {
        this.head = new Node(-999);
        this.tail = head;
    }

    public int get(int index) {
        Node result = head.getNext();
        int i = 0;

        while (result != null) {
            if (i == index) return result.getValue();

            i++;
            result = result.getNext();
        }

        return -1;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);

        newNode.setNext(head.getNext());
        head.setNext(newNode);

        if (newNode.getNext() == null) {
            tail = newNode;
        }
    }

    public void insertTail(int val) {
        this.tail.setNext(new Node(val));
        this.tail = this.tail.getNext();
    }

    public boolean remove(int index) {
        int i = 0;
        Node current = this.head;

        while (i < index && current != null) {
            i++;
            current = current.getNext();
        }

        if (current != null && current.getNext() != null) {
            if (current.getNext() == this.tail) this.tail = current;

            current.setNext(current.getNext().getNext());
            return true;
        }

        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> res = new ArrayList<>();
        Node curr = this.head.getNext();
        while (curr != null) {
            res.add(curr.getValue());
            curr = curr.getNext();
        }
        return res;
    }
}
