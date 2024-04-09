import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { AuthComponent } from './auth/auth.component';
import { MainComponent } from './main/main.component';

const routes: Routes = [
  {path:'', component: MainComponent},
  {path: 'auth', loadChildren:()=>import('./auth/auth.module').then(m=>m.AuthModule)},
  {path: 'dash', loadChildren:()=>import('./dash/dash.module').then(m=>m.DashModule)}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
