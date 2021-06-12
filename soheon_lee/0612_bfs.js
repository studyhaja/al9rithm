
const bfs = (root) => {
  if (root === []) {
    return 0
  }
  
  if (root.length === 1) {
    return 1
  }
  
  let finalDepth = 1
  
  const findValue = (root, depth) => {
    if (!(root[Math.pow(2,(depth-1)) -1] === undefined)) {
      console.log('element exists')
      depth += 1;
      finalDepth = depth
      console.log('depth: ', depth)
      bfs(root.slice(Math.pow(2,(depth-1))))
    }
  }

  findValue(root, 1)

  return finalDepth
  
}
