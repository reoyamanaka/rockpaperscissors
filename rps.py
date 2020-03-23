import wx, sys

app = wx.App()
window = wx.Frame(None, title = "Rock Paper Scissors", size = (560, 300))
panel = wx.Panel(window)

#Funciton and button to terminate program from panel
def terminate(event):
    sys.exit()

#instructions
controls = wx.StaticText(panel, label = "f - Rock, g - Paper, h - Scissors (lower-case).", pos = (60, 45))

#larger font and controls label
larger_font = wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
controls_label = wx.StaticText(panel, label = "Controls", pos = (60, 6))
controls_label.SetFont(larger_font)

#player1 move entry
player_command = wx.StaticText(panel, label = "Player 1: Type in your letter. Note: HIDE YOUR FINGERS WHEN YOU TYPE! \nInput is in white text (invisible).", pos = (60, 70))
player_input = wx.TextCtrl(panel, pos = (60, 115), size = (20, 23))
player_input.SetForegroundColour((255,255,255))

#Function to take first input
def submit_first_move(event):
    global player1_move
    player1_move = player_input.GetValue()
    print(player1_move)

    player_command.SetLabel("Player 1's move submitted. Player 2: Type in your letter.\nNote: HIDE YOUR FINGERS WHEN YOU TYPE!")
    player_input.Clear()

    submit_button1.Hide()

    global submit_button2
    submit_button2 = wx.Button(panel, label = "Submit move: Player 2", pos = (60, 150))
    submit_button2.Bind(wx.EVT_BUTTON, submit_second_move)

#Function to take second input
def submit_second_move(event):
    player2_move = player_input.GetValue()
    print(player2_move)

    player_command.SetLabel("Player 2's move submitted. Let's see who wins!")

    player_input.Hide()
    submit_button2.Hide()

    if player1_move == "f" or player1_move == "g" or player1_move == "h":
        if player2_move == "f" or  player2_move == "g" or player2_move == "h":
#rock and paper, vice versa
            if player1_move == "f" and player2_move == "g":
                player_command.SetLabel("Player 1 played ROCK and Player 2 played PAPER. Player 2 wins!")

            elif player1_move == "g" and player2_move == "f":
                player_command.SetLabel("Player 1 played PAPER and Player 2 played ROCK. Player 1 wins!")

#rock and scissors, vice versa
            elif player1_move == "f" and player2_move == "h":
                player_command.SetLabel("Player 1 played ROCK and Player 2 played SCISSORS. Player 1 wins!")
            elif player1_move == "h" and player2_move == "f":
                player_command.SetLabel("Player 1 played SCISSORS and Player 2 played ROCK. Player 2 wins!")

#scissors and paper, vice versa
            elif player1_move == "h" and player2_move == "g":
                player_command.SetLabel("Player 1 played SCISSORS and Player 2 played PAPER. Player 1 wins!")
            elif player1_move == "g" and player2_move == "h":
                player_command.SetLabel("Player 1 played PAPER and Player 2 played SCISSORS. Player 2 wins!")

            elif player1_move == player2_move:
                player_command.SetLabel("It's a draw!")
        else:
            player_command.SetLabel("Invalid input(s). Press Reset.")
    else:
        player_command.SetLabel("Invalid input(s). Press Reset.")
        
submit_button1 = wx.Button(panel, label = "Submit move: Player 1", pos = (60, 150))
submit_button1.Bind(wx.EVT_BUTTON, submit_first_move)

#function to reset game
def reset_game(event):
    global player1_move, player2_move, player_input, player_command, submit_button1, submit_button2
    submit_button1.Show()
    player_input.Clear()
    player_input.Show()
    player_command.SetLabel("Player 1: Type in your letter. Note: HIDE YOUR FINGERS! \nInput is in white text (invisible).")
    
reset_button = wx.Button(panel, label = "Reset", pos = (60, 210))
reset_button.Bind(wx.EVT_BUTTON, reset_game)

terminate_button = wx.Button(panel, label = "Terminate", pos = (60, 240))
terminate_button.Bind(wx.EVT_BUTTON, terminate)

window.Show(True)
app.MainLoop()
