import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    function.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title('To-do App')
st.subheader('Add new items or click on the existing ones when complete:')

for index, items in enumerate(todos):
    checkbox = st.checkbox(items, key=items)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[items]
        st.rerun()

st.text_input(' ', placeholder='Type an item here and press ENTER..',
              on_change=add_todo, key='new_todo')