#include <iostream>
#include <thread>
#include <chrono>
#include <optional>
#include <string>
#include <sstream>
#include <conio.h>
#include <windows.h>

void showNotification(const std::string& title, const std::string& message) {
    MessageBoxA(NULL, message.c_str(), title.c_str(), MB_OK | MB_ICONINFORMATION);
}

void startTimer(int workInterval, int breakIntrval, 
                const std::string& workMessage = "It's work time!", 
                const std::string& breakMessage = "It's break time!") {
    
    bool ifWorking = true;
    int minutesLeft = workInterval;

    bool running = true;
    while (running) {
        // Display time left
        std::cout << (ifWorking ? "Working" : "Break") << "... (" << minutesLeft 
                  << " minute" << (minutesLeft  == 1 ? " " : "s ") << "left)             \r";

        // Wait 1 minute (2s * 30)
        for (int i=0; i < 30; i++) {
            std::this_thread::sleep_for(std::chrono::seconds(2));
            // Check if Enter is pressed for exiting the programm
            if (_kbhit()){
                char input = _getch();
                if (input == '\r'){
                    std::cout << "Exiting break reminder.                                \n";
                    running = false;
                    break;
                }
            }
        }
        minutesLeft--;
        
        // Whether interval is finnished
        if (minutesLeft <= 0) {
            // Work is finnished
            if (ifWorking){
                showNotification("Break time", breakMessage + " (" + std::to_string(breakIntrval) + " min)\n");
                ifWorking = false;
                minutesLeft = breakIntrval;
            } 
            // Work is finnished
            else {
                showNotification("Work time", workMessage + " (" + std::to_string(workInterval) + " min)\n");
                ifWorking = true;
                minutesLeft = workInterval;
            }
        }
    }
}

std::optional<int> getValidInt(int minVal = 1, int maxVal = 1440,
                const std::string& errorMsg = "Invalid input. Please enter valid integer: ") {
    std::string input;
    int value;
    while (true) {
        std::getline(std::cin, input);

        if (input.empty()) return std::nullopt;

        std::istringstream iss_val(input);
        iss_val >> value;

        if (iss_val.fail() || !iss_val.eof()) std::cout << errorMsg;

        else if (value < minVal || value > maxVal){
            std::cout << "Invalid input. Please enter integer value in range " << minVal << " - " << maxVal << ": ";

        } else return value;
    }
}

int main() {
    // Utils
    int workTime = 45; // minutes
    int breakTime = 15; // minutes
    std::optional<int> input = std::nullopt;

    // Display interface
    std::cout << "\n===============================\n";
    std::cout << " - WELCOME TO BREAK REMINDER - \n";
    std::cout << "===============================\n\n";
    
    std::cout << "Please set prefered length of WORK interval (in minutes) [" << workTime << "]: ";
    workTime = getValidInt().value_or(workTime);
    std::cout << "\nPlease set prefered length of BREAK interval (in minutes) [" << breakTime << "]: ";
    breakTime = getValidInt().value_or(breakTime);

    std::cout << "\nWork time is set to:  " << workTime << " min." << std::endl;
    std::cout << "Break time is set to: " << breakTime << " min." << std::endl << std::endl;
    std::cout << "The break reminder is working in the background." << std::endl;
    std::cout << "You will be notified when the current interval is finished." << std::endl;
    std::cout << "To exit the program, press ENTER."
              << " Ensure this window is selected (active) before pressing." << std::endl << std::endl;

    // Start the timer
    startTimer(workTime, breakTime);

    return 0;
}
