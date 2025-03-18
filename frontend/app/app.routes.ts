import { Routes, RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { HomeComponent } from './home/home.component';
import { TodoComponent } from './todo/todo.component';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'todo', component: TodoComponent },
];

@NgModule({ 
    imports: [RouterModule.forChild(routes)], 
    exports: [RouterModule], 
}) 
export class AppRoutingModule { } 
