    def game_control(self):
        btn = self.sender()
        text = btn.text()
        if text and btn == self.btn_list[0]:
            if self.btn_list[1].text() == "":
                self.btn_list[0].setText(self.btn_list[1].text())
                self.btn_list[1].setText(text)
            elif self.btn_list[4].text() == "":
                self.btn_list[0].setText(self.btn_list[4].text())
                self.btn_list[4].setText(text)
        elif text and btn == self.btn_list[1]:
            if self.btn_list[0].text() == "":
                self.btn_list[1].setText(self.btn_list[0].text())
                self.btn_list[0].setText(text)
            elif self.btn_list[2].text() == "":
                self.btn_list[1].setText(self.btn_list[2].text())
                self.btn_list[2].setText(text)
            elif self.btn_list[5].text() == "":
                self.btn_list[1].setText(self.btn_list[5].text())
                self.btn_list[5].setText(text)

        elif text and btn == self.btn_list[2]:
            if self.btn_list[1].text() == "":
                self.btn_list[2].setText(self.btn_list[1].text())
                self.btn_list[1].setText(text)
            elif self.btn_list[3].text() == "":
                self.btn_list[2].setText(self.btn_list[3].text())
                self.btn_list[3].setText(text)
            elif self.btn_list[6].text() == "":
                self.btn_list[2].setText(self.btn_list[6].text())
                self.btn_list[6].setText(text)
        elif text and btn == self.btn_list[3]:
            if self.btn_list[2].text() == "":
                self.btn_list[3].setText(self.btn_list[2].text())
                self.btn_list[2].setText(text)
            elif self.btn_list[7].text() == "":
                self.btn_list[3].setText(self.btn_list[7].text())
                self.btn_list[7].setText(text)
        
        elif text and btn == self.btn_list[4]:
            if self.btn_list[0].text() == "":
                self.btn_list[4].setText(self.btn_list[0].text())
                self.btn_list[0].setText(text)
            elif self.btn_list[5].text() == "":
                self.btn_list[4].setText(self.btn_list[5].text())
                self.btn_list[5].setText(text)
            elif self.btn_list[8].text() == "":
                self.btn_list[4].setText(self.btn_list[8].text())
                self.btn_list[8].setText(text)
        
        elif text and btn == self.btn_list[5]:
            if self.btn_list[1].text() == "":
                self.btn_list[5].setText(self.btn_list[1].text())
                self.btn_list[1].setText(text)
            elif self.btn_list[4].text() == "":
                self.btn_list[5].setText(self.btn_list[4].text())
                self.btn_list[4].setText(text)
            elif self.btn_list[6].text() == "":
                self.btn_list[5].setText(self.btn_list[6].text())
                self.btn_list[6].setText(text)
            elif self.btn_list[9].text() == "":
                self.btn_list[5].setText(self.btn_list[9].text())
                self.btn_list[9].setText(text)

        elif text and btn == self.btn_list[6]:
            if self.btn_list[2].text() == "":
                self.btn_list[6].setText(self.btn_list[2].text())
                self.btn_list[2].setText(text)
            elif self.btn_list[5].text() == "":
                self.btn_list[6].setText(self.btn_list[5].text())
                self.btn_list[5].setText(text)
            elif self.btn_list[7].text() == "":
                self.btn_list[6].setText(self.btn_list[7].text())
                self.btn_list[7].setText(text)
            elif self.btn_list[10].text() == "":
                self.btn_list[6].setText(self.btn_list[10].text())
                self.btn_list[10].setText(text)
            if self.btn_list[6] =='6':
                self.btn_list[6] = self.setStyleSheet("backround-color: green")
        elif text and btn == self.btn_list[7]:
            if self.btn_list[3].text() == "":
                self.btn_list[7].setText(self.btn_list[3].text())
                self.btn_list[3].setText(text)
            elif self.btn_list[6].text() == "":
                self.btn_list[7].setText(self.btn_list[6].text())
                self.btn_list[6].setText(text)
            elif self.btn_list[11].text() == "":
                self.btn_list[7].setText(self.btn_list[11].text())
                self.btn_list[11].setText(text)

        # Diyorbekning varianti
        elif text and btn == self.btn_list[8]:
            if self.btn_list[4].text() == "":
                self.btn_list[8].setText(self.btn_list[4].text())
                self.btn_list[4].setText(text)
            elif self.btn_list[9].text() == "":
                self.btn_list[8].setText(self.btn_list[9].text())
                self.btn_list[9].setText(text)
            elif self.btn_list[12].text() == "":
                self.btn_list[8].setText(self.btn_list[12].text())
                self.btn_list[12].setText(text)
        elif text and btn == self.btn_list[9]:
            if self.btn_list[5].text() == "":
                self.btn_list[9].setText(self.btn_list[5].text())
                self.btn_list[5].setText(text)
            elif self.btn_list[8].text() == "":
                self.btn_list[9].setText(self.btn_list[8].text())
                self.btn_list[8].setText(text)
            elif self.btn_list[10].text() == "":
                self.btn_list[9].setText(self.btn_list[10].text())
                self.btn_list[10].setText(text)
            elif self.btn_list[13].text() == "":
                self.btn_list[9].setText(self.btn_list[13].text())
                self.btn_list[13].setText(text)

        elif text and btn == self.btn_list[10]:
            if self.btn_list[6].text() == "":
                self.btn_list[10].setText(self.btn_list[6].text())
                self.btn_list[6].setText(text)
            elif self.btn_list[9].text() == "":
                self.btn_list[10].setText(self.btn_list[9].text())
                self.btn_list[9].setText(text)
            elif self.btn_list[11].text() == "":
                self.btn_list[10].setText(self.btn_list[11].text())
                self.btn_list[11].setText(text)
            elif self.btn_list[14].text() == "":
                self.btn_list[10].setText(self.btn_list[14].text())
                self.btn_list[14].setText(text)
        elif text and btn == self.btn_list[11]:
            if self.btn_list[7].text() == "":
                self.btn_list[11].setText(self.btn_list[7].text())
                self.btn_list[7].setText(text)
            elif self.btn_list[10].text() == "":
                self.btn_list[11].setText(self.btn_list[10].text())
                self.btn_list[10].setText(text)
            elif self.btn_list[15].text() == "":
                self.btn_list[11].setText(self.btn_list[15].text())
                self.btn_list[15].setText(text)
        
        elif text and btn == self.btn_list[12]:
            if self.btn_list[8].text() == "":
                self.btn_list[12].setText(self.btn_list[8].text())
                self.btn_list[8].setText(text)
            elif self.btn_list[13].text() == "":
                self.btn_list[12].setText(self.btn_list[13].text())
                self.btn_list[13].setText(text)
        
        elif text and btn == self.btn_list[13]:
            if self.btn_list[9].text() == "":
                self.btn_list[13].setText(self.btn_list[9].text())
                self.btn_list[9].setText(text)
            elif self.btn_list[12].text() == "":
                self.btn_list[13].setText(self.btn_list[12].text())
                self.btn_list[12].setText(text)
            elif self.btn_list[14].text() == "":
                self.btn_list[13].setText(self.btn_list[14].text())
                self.btn_list[14].setText(text)

        elif text and btn == self.btn_list[14]:
            if self.btn_list[10].text() == "":
                self.btn_list[14].setText(self.btn_list[10].text())
                self.btn_list[10].setText(text)
            elif self.btn_list[13].text() == "":
                self.btn_list[14].setText(self.btn_list[13].text())
                self.btn_list[13].setText(text)
            elif self.btn_list[15].text() == "":
                self.btn_list[14].setText(self.btn_list[15].text())
                self.btn_list[15].setText(text)
        
        elif text and btn == self.btn_list[15]:
            if self.btn_list[11].text() == "":
                self.btn_list[15].setText(self.btn_list[11].text())
                self.btn_list[11].setText(text)
            elif self.btn_list[14].text() == "":
                self.btn_list[15].setText(self.btn_list[14].text())
                self.btn_list[14].setText(text)