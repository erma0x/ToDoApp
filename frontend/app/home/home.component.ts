import { Component } from '@angular/core';
import { Router, RouterModule, Routes } from '@angular/router';

@Component({
  selector: 'app-home',
  imports: [],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css','../app.component.css']
})
export class HomeComponent {
  constructor(private router: Router) { }

  ngOnInit() { }

  redirectToDo() {
      this.router.navigate(['/todo']);
  }
}
