# This program prints Hello, world!
--- 
- name: "Python Script run"
  become: true
  gather_facts: false
  hosts: all
  strategy: free
  tasks: 
    - name: Run the HelloWorld File
      command: python3 HelloWorld.py
