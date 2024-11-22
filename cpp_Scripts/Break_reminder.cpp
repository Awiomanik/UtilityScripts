#include <iostream>
#include <thread>
#include <chrono>
#include <string>
#include <windows.h>

void showNotification(const std::string& title, const std::string& message) {
    MessageBoxA(NULL, message.c_str(), title.c_str(), MB_OK | MB_ICONINFORMATION);
}

void startTimer(int workInterval, int breakIntrval, 
                const std::string& workMessage = "It's work time!", 
                const std::string& breakMessage = "It's break time!") {
    
    bool ifWorking = true;
    int minutesLeft = workInterval;

    while (true) {
        // Wait 1 minute
        std::cout << std::endl << (ifWorking ? "Working" : "Break") << "... " << minutesLeft << "minutes left.   \r"; // minute to minutes depending on number
        std::this_thread::sleep_for(std::chrono::minutes(1));
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

int getValidInt(int minVal = 1, int maxVal = 1440,
                const std::string& errorMsg = "Invalid input. Please enter valid integer: ") {
    int value;
    while (true) {
        std::cin >> value;

        if (std::cin.fail()) {
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            std::cout << errorMsg;
        } else if (value < minVal || value > maxVal){
            std::cout << "Invalid input. Please enter integer value in range " << minVal << " - " << maxVal << ": ";
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard extra input
            return value;
        }
    }
}

int main() {
    int workTime = 45; // minutes
    int breakTime = 15; // minutes


    std::cout << "\n===============================\n";
    std::cout << " - WELCOME TO BREAK REMINDER - \n";
    std::cout << "===============================\n\n";
    
    std::cout << "Please set prefered length of WORK interval: ";
    workTime = getValidInt();
    std::cout << "\nPlease set prefered length of BREAK interval: ";
    breakTime = getValidInt();

    std::cout << std::endl << "Work time is set to: " << workTime << "min." << std::endl;
    std::cout << "Break time is set to: " << breakTime << "min." << std::endl << std::endl;
    std::cout << "Break reminder is working in the background." << std::endl;
    std::cout << "You will be notified when the current interval is finnished." << std::endl;
    std::cout << "To exit the programm You can terminate it with ctrl + C shortcut."; // Change it

    // Start the timer
    startTimer(workTime, breakTime);

    return 0;
}
