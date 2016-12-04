## Codesters Bike Challenge

										Dec 6, 2016


  * Start the Bicycle game
    * Go to link https://hourofcode.com/codestersflappybike
    * Press the Play button (green button with > icon)
    * Quickly press the space bar consecutively to keep the bicycle in the sky.
    * Play the game, a few seconds, to keep the bicycle from colliding into the blue rectangles.
    * Click the Stop button (red button with rectangle icon)

  * Change the background to Underwater
    * Click on STAGE Codestrs category in left hand menu
    * Highlight this line of code by double clicking
      * stage.set_background(“city”)
    * Double click “Underwater” in the left hand menu to change the background
    * Verify the line of code now is
      * stage.set_background(“underwater”)
    * Click Play

  * Change the background to a Fish
    * Click on SPRITE Codestrs category in left hand menu
    * Highlight this line of code by double clicking
       * sprite = codestrs.Sprite(“bike”)
    * Double click “Fish 1” in the left hand menu to change the sprite icon
    * Verify the line of code now is
       * sprite = codestrs.Sprite(“fish”)
    * Click Play

  * **Start coding!!**
    * Basic Grid
       * Copy the Python code into your editor https://raw.githubusercontent.com/llevans/Codestrs/master/codestrs_grid.py
       * Click Play
       * Click the Right Arrow – the keyboard event triggers the bike to start and stop pedalling

    * Flip the bike 360 degrees when the Left Arrow is clicked
       * Copy codestrs_flip_360.py into your editor https://raw.githubusercontent.com/llevans/Codestrs/master/codestrs_flip_360.py
       * Click Play
          * Click the “Right Arrow” – the keyboard event triggers the bike to start and stop pedalling
          * Click the “Left Arrow" – the keyboard event triggers the bike the flip

       * Assignment – Update the codestrs_flip_forloop_assign Python script to calculate the rotation in a for loop
          * Copy  codestrs_flip_forloop_assign.py into your editor https://raw.githubusercontent.com/llevans/Codestrs/master/codestrs_flip_forloop_assign.py
          * Update the code at line 29 to rotate the bike position inside a for loop
          * Click Play

    * Make the bike jump when the "Up Arrow" key is clicked
       * Assignment – Update the codestrs_jump_onupkey_assign Python script with to handle the "Up Arrow" key event
          * Copy  codestrs_flip_forloop_assign.py into your editor https://raw.githubusercontent.com/llevans/Codestrs/master/codestrs_jump_onupkey_assign.py
          * Update the code at line 38 to 
               * retain the bike’s current X, Y position
               * call the sprint jump() API method
               * return the bike to it’s original position
          * Click Play




###MIT App Inventor Setup: -
   * Install the Emulator –
      * Go To link http://appinventor.mit.edu/explore/ai2/setup.html
      * Click ‘Build your project on your computer’ for Option Two, Use the Emulator
      * Click on the Instructions for your OS.
      * Click on the downloaded package to install the App Inventor Emulator
      * Install the App Inventor companion
          * https://play.google.com/store/apps/details?id=edu.mit.appinventor.aicompanion3&hl=en
 
   * Build an Android App in App Inventor -

      * Go to link http://code.appinventor.mit.edu/
      * Click Continue without an Account
      * Click Start New Project – TalkToMeApp
      * Click Connect – Emulator
      * Click GO to connect the App Inventor Studio to the aiStarter
      * Add a Button
         * Our project needs a button. Click and hold on the word "Button" in the palette. Drag your mouse over to the Viewer. Drop the button and a new button will appear on the Viewer.
6.	

