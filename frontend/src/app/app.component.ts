import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Vighna AI';
  activeTab = 'chat';

  selectTab(tab: string) {
    this.activeTab = tab;
  }
}
