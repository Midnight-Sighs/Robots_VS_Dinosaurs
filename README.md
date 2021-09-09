# Robots_VS_Dinosaurs

Welcome to Robots vs Dinosaurs.  This is where you'll pick one or the other and try to bash them!  Let's be honest, the dinosaurs should win every time.  


***

Algorithm write out before coding (I feel like I'm missing something as this seems way too simple)
"As a developer, I want the battle to conclude once either all the robots in the Fleet have their health points reach zero or all of the dinosaurs in the Herd have their health points reach zero."
    - at the end of each turn, loop through the creatures' HP to see if any of them are over 0
    - any creatures that are at 0 HP, they are removed from the list
    - if the list is empty (as all have been removed for having 0 HP):
        - break out of all other turn/stuffs to initiate new function
    - new function is essentially "the end credits".  Praises you and congratulates you and dares you to try to do battle again.  
    - if during the loop through there are creatures that still have over 0 HP, turn continues as normal

***

- first commit was just initial set up
- second commit: I think I have a good scaffolding to work from.  Mostly been inputting data, taking notes, and putting a plan together.  But I think I have a good starting place.  
- third commit: I think I'm getting the hang of Python, importing, and classes.  More scaffolding written but all untested as it hasn't all been pulled onto the Battlefield yet.  Getting there.
- fourth commit: You can now select weapons for the robots after you select them.  