import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ExpiryHomeComponent } from './home/Expiry-home.component';
import { ExpiryNewComponent } from './new/Expiry-new.component';
import { ExpiryDetailComponent } from './detail/Expiry-detail.component';

const routes: Routes = [
  {path: '', component: ExpiryHomeComponent},
  { path: 'new', component: ExpiryNewComponent },
  { path: ':id', component: ExpiryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Expiry-detail-permissions'
      }
    }
  }
];

export const EXPIRY_MODULE_DECLARATIONS = [
    ExpiryHomeComponent,
    ExpiryNewComponent,
    ExpiryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ExpiryRoutingModule { }