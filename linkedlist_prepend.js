// add a method prepend() to the linked list that adds a node to the beginning of the list

class LinkedList {
    constructor(value) {
      this.head = {
        value: value,
        next: null
      };
      this.tail = this.head;
      this.length = 1;
    }
    append(value) {
      const newNode = {
        value: value,
        next: null
      }
      console.log(newNode)
      this.tail.next = newNode;
      this.tail = newNode;
      this.length++;
      return this;
    }
    prepend(value) {
      //Code here
      const newNode = {
          value: value,
          next: null,
      }
      newNode.next = this.head;
      this.head = newNode;
      this.length++;
      return this
    }
  }
  
  let myLinkedList = new LinkedList(10);
  console.log(myLinkedList.append(5));
  console.log(myLinkedList.append(16));
  console.log(myLinkedList.prepend(1))
  