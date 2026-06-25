class Node {
public:
    int val;
    Node* next;

    Node() : val(0), next(nullptr) {}
    Node(int val) : val(val), next(nullptr) {}

    virtual ~Node() {

    }
};

class LinkedList{
public:
    Node* head;
    Node* tail;

    LinkedList() : head(nullptr), tail(nullptr) {}
    virtual ~LinkedList() {
        Node* traverseNode = head;
        while(traverseNode) {
            Node* tempNode = traverseNode;
            traverseNode = traverseNode->next;
            delete tempNode;
        }
    }

    void insertHead(int val) {
        Node* newNode = new Node(val);
        if (!head) {
            head = newNode;
            tail = head;
        } else {
            newNode->next = head;
            head = newNode;
        }
    }

    void insertTail(int val) {
        if (!head) insertHead(val);
        else {
            Node* newNode = new Node(val);
            tail->next = newNode;
            tail = newNode;
        }
    }

    void printList() {
        Node* traverseNode = head;

        std::cout << "[";
        while(traverseNode) {
            std::cout << traverseNode->val;
            traverseNode = traverseNode->next;
            if (traverseNode) std::cout << ", ";
        }

        std::cout << "]" << std::endl;
    }

    int get(int index) {
        if ((index < 0) || (!head)) return -1;
        int traverseIndex = 0;
        Node* traverseNode = head;

        while(traverseNode && (traverseIndex++ < index)) traverseNode = traverseNode->next;

        if (traverseNode) return traverseNode->val;
        else return -1;
    }

    bool remove(int index) {
        if ((index < 0) || !head) return false;

        if (index == 0) {
            if (head == tail) {
                delete head;
                head = tail = nullptr;
            } else {
                Node* tempNode = head;
                head = head->next;
                if (!head) tail = nullptr;
                delete tempNode;
            }
        } else {
            int traverseIndex = 1;
            Node* back = head;
            Node* front = head->next;

            while(front && (traverseIndex++ < index)) {
                front = front->next;
                back = back->next;
            }

            if (front) {
                Node* tempNode = front;
                back->next = front->next;
                if (front == tail) tail = back;
                delete tempNode;
            } else {
                return false;
            }

        }

        return true;
    }

    vector<int> getValues() {
        vector<int> nodeList;

        Node* traverseNode = head;
        while(traverseNode) {
            nodeList.push_back(traverseNode->val);
            traverseNode = traverseNode->next;
        }
        return nodeList;
    }
};
