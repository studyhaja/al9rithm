class Stack2 {
  constructor(){
    this.array = [];
  }

  peek() {
    return this.array[array.length()-1]
  }

  push(value){
    return this.array.push(value)
  }

  pop(){
    return this.array.pop()
  }
}

class Node {
  constructor(value){
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor(){
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }
  
  peek() {
    if (this.top) {
      return this.top.value
    }
    return this.top
  }
  push(value) {
    let newNode = new Node(value)
    newNode.next = this.top
    this.top = newNode
    this.length++
  }
  pop() {
    if (this.top) {
      const result = this.top.value
      this.top = this.top.next
      this.length--
      return result
    }
    return this.top
  }
}

bb = new Stack()
bb.push(1)
bb.push(2)
bb.push(3)

bb.pop()

console.log('bbbbbbb', bb)
