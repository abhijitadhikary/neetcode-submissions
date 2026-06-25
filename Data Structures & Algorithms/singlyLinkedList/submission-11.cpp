class Node {
public:
    int val;
    Node* next;
    Node (int val) : val(val), next(nullptr) {}
    virtual ~Node() {
        next = nullptr;
    }
};

class LinkedList {
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
            tempNode = nullptr;
        }
        head = tail = nullptr;
    }

    int get(int index) {
        if ((index < 0) || (!head)) return -1;

        Node* traverseNode = head;

        int traverseIndex = 0;
        while(traverseNode && (traverseIndex++ < index)) {
            traverseNode = traverseNode->next;
        }

        if (traverseNode) return traverseNode->val;
        else return -1;
    }

    void insertHead(int val) {
        Node* newNode = new Node(val);
        if (!head) head = tail = newNode;
        else {
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

    bool remove(int index) {
        if ((index < 0) || (!head)) return false;

        if (index == 0) {
            if (head == tail) {
                delete head;
                head = tail = nullptr;
            } else {
                Node* tempNode = head;
                head = head->next;
                delete tempNode;
                tempNode = nullptr;
            }
        } else {
            int traverseIndex = 1;
            Node* back = head;
            Node* front = head->next;

            while(front && (traverseIndex++ < index)) {
                back = back->next;
                front = front->next;
            }

            if (front) {
                back->next = front->next;
                if (front == tail) tail = back;
                delete front;
                front = nullptr;
            } else return false;
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
