import streamlit as st
import random
st.title("guess the number of game")

# generate a random number between 1 and 100
number = random.randint(1,100)

guess = st.number_input("Enter a number (between 1 and 100):", min_value=1,max_value=100)

if st.botton("Make a guess!"):
  if guess > number:
    st.write("Too high! Try a small number.")
  elif guess < number:
    st.write("Too low! Tyr a large number.")
  else:
    st.write("congratulations! You have guessed the number correctly.")
