//
//  ViewController.swift
//  TapperProject
//
//  Created by Asaia Palacios on 5/25/16.
//  Copyright © 2016 Asaia Palacios. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    // Define variables
    var taps_requested: Int? = 0
    var taps_done: Int = 0
    
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    
    @IBAction func clickPlayButton(sender: AnyObject) {
        if textfield_number.text != nil && textfield_number.text != "" {
            taps_requested = Int(textfield_number.text!)
            print("Let's do \(self.textfield_number.text) taps")
        }
        if taps_requested > 0 {
            self.initGame()
        }
    }
    
    // Make int 0 to str then store in self.label_taps.text
    func updateTapsLabel() {
        self.label_taps.text = String(self.taps_done) + " taps !"
    }
    
    @IBAction func clickCoinButton(sender: AnyObject) {
        self.taps_done += 1                                         // Increase taps by 1

        print("Tap!")
        self.updateTapsLabel()
        if self.taps_done >= self.taps_requested {
            self.resetGame()
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.resetGame()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func initGame() {
        self.taps_done = 0
        self.updateTapsLabel()
        
        self.image_tapper.hidden = true
        self.textfield_number.hidden = true
        self.button_play.hidden = true
        
        self.button_coin.hidden = false
        self.label_taps.hidden = false
    }
    
    func resetGame() {
        self.taps_requested = 0
        
        self.image_tapper.hidden = false
        self.textfield_number.hidden = false
        self.button_play.hidden = false
        
        self.button_coin.hidden = true
        self.label_taps.hidden = true
    }

}

